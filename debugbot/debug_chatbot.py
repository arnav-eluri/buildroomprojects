import ast
import py_compile
import tempfile
import os
import sys
import traceback

def check_syntax(code):
    try:
        ast.parse(code)
        return None
    except SyntaxError as e:
        return {
            "type": "SyntaxError",
            "message": e.msg,
            "line": e.lineno,
            "offset": e.offset,
            "text": e.text.strip() if e.text else ""
        }

def check_compilation(code):
    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write(code)
            temp_path = f.name
        py_compile.compile(temp_path, doraise=True)
        return None
    except py_compile.PyCompileError as e:
        return {"type": "CompileError", "message": str(e)}
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

def check_common_bugs(code):
    issues = []
    lines = code.split("\n")

    for i, line in enumerate(lines, 1):
        stripped = line.strip()

        if stripped.startswith("def ") or stripped.startswith("class ") or stripped.startswith("if ") or stripped.startswith("elif ") or stripped.startswith("else") or stripped.startswith("for ") or stripped.startswith("while ") or stripped.startswith("try") or stripped.startswith("except") or stripped.startswith("with "):
            if stripped.endswith(":"):
                continue
            if stripped.startswith("else") and stripped.strip() == "else":
                continue
            if stripped.startswith("elif ") and stripped.endswith(":"):
                continue
            if stripped.startswith("except") and stripped.endswith(":"):
                continue
            if not stripped.endswith(":"):
                keyword = stripped.split()[0]
                issues.append(f"Line {i+1}: Missing colon `:` after `{keyword}` statement")

    if "    " in line and not line.startswith("    ") and line.strip():
        leading_spaces = len(line) - len(line.lstrip())
        if leading_spaces > 0 and leading_spaces % 4 != 0:
            issues.append(f"Line {i+1}: Inconsistent indentation (found {leading_spaces} spaces, expected multiple of 4)")

    if "==" in line and "if " in line:
        if "= True" in line or "= False" in line:
            pass

    if "import " in line and line.strip().startswith("import "):
        parts = line.strip().split()
        if len(parts) >= 2:
            mod = parts[1].split(".")[0].split(" as ")[0].strip()
            if mod in KNOWN_STDLIB:
                continue

    if "input" in line and "eval" in line:
        issues.append(f"Line {i+1}: Using `eval(input(...))` is a security risk. Consider using `int(input(...))` or `float(input(...))` instead.")

    if "os.system" in line or "subprocess.call" in line:
        issues.append(f"Line {i+1}: Using `os.system` or `subprocess.call` with user input can be a security risk.")

    if "except:" in line.strip() and line.strip() == "except:":
        issues.append(f"Line {i+1}: Bare `except:` catches all exceptions. Consider using `except Exception:` instead.")

    if "while True" in line and "break" not in code:
        issues.append(f"Line {i+1}: `while True` loop without a `break` statement — this will run forever.")

    if "=" in line and "==" in line:
        parts = line.split("==")
        if len(parts) == 2 and "=" in parts[0].strip():
            assign_part = parts[0].strip()
            if "=" in assign_part and "==" not in assign_part.split("=")[0]:
                issues.append(f"Line {i+1}: Possible assignment `=` inside a condition. Did you mean `==`?")

    if "except:" in line.strip() and line.strip() == "except:":
        issues.append(f"Line {i+1}: Bare `except:` catches all exceptions. Use `except Exception:` instead.")

    if "while True" in line and "break" not in code:
        issues.append(f"Line {i+1}: `while True` loop without a `break` — this will run forever.")

    if "if " in line and ":" in line:
        if "= " in line.split(":")[0] and "==" not in line.split(":")[0]:
            issues.append(f"Line {i+1}: Using `=` (assignment) instead of `==` (comparison) in condition.")

    if "open(" in line and ".close()" not in code:
        issues.append(f"Line {i+1}: File opened with `open()` but no `.close()` found. Consider using a `with` statement.")

    if "print(" in line and "f" in line and "'" in line:
        if "f'" in line or 'f"' in line:
            pass

    if "range(" in line and "len(" in line:
        issues.append(f"Line {i+1}: Using `range(len(...))` — consider using `enumerate()` for cleaner code.")

    if "==" in line and "if " in line:
        if "None" in line.split("==")[1]:
            issues.append(f"Line {i+1}: Use `is None` instead of `== None` for comparing with None.")

    if "is" in line and "if " in line:
        if "== " in line:
            pass

    if "finally:" in code and "try:" not in code:
        issues.append("Found `finally:` without a matching `try:` block.")

    if "except" in code and "try:" not in code:
        issues.append("Found `except` without a matching `try:` block.")

    if "elif " in code and "if " not in code:
        issues.append("Found `elif` without a matching `if` statement.")

    return issues

def analyze_code(code):
    results = []

    syntax_error = check_syntax(code)
    if syntax_error:
        results.append(f"[Syntax Error] Line {syntax_error['line']}: {syntax_error['message']}")
        if syntax_error.get("text"):
            results.append(f"  -> {syntax_error['text']}")
            if syntax_error.get("offset"):
                results.append(f"     {' ' * (syntax_error['offset'] - 1)}^")
        return results

    compile_error = check_compilation(code)
    if compile_error:
        results.append(f"[Compile Error] {compile_error['message']}")
        return results

    common_issues = check_common_bugs(code)
    results.extend(common_issues)

    if not results:
        results.append("No obvious issues found. The code looks clean!")

    return results

def main():
    print("=" * 60)
    print("  DebugBot — Code Debug Assistant")
    print("  Paste your code below and I'll analyze it for bugs.")
    print("  Type 'exit' to quit.")
    print("=" * 60)

    while True:
        print("\n--- Paste your code (type 'DONE' on its own line when finished, or 'exit' to quit) ---")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "DONE":
                break
            if line.strip().lower() == "exit":
                print("Goodbye!")
                return
            lines.append(line)

        code = "\n".join(lines)
        if not code.strip():
            print("No code entered. Try again.")
            continue

        print("\n[ Analyzing... ]\n")
        results = analyze_code(code)

        if not results:
            print("No issues found. The code looks clean!")
        else:
            print(f"Found {len(results)} potential issue(s):\n")
            for r in results:
                print(f"  - {r}")

        print("\n" + "-" * 60)

if __name__ == "__main__":
    main()
