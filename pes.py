import g4f
import sys
import pyperclip
try:
    args = ''

    for i in sys.argv:
        if not i == sys.argv[0]:
            args = args + ' ' + i

    response = g4f.ChatCompletion.create(
        model='llama-3.1-70b',
        messages=[{"role": "user", "content": str(args)}],
        stream=True
    )
    x = ''
    for message in response:
        print(message, flush=True, end='')
        x = x + message
        
    pyperclip.copy(x)

except Exception as exc:
    print(exc)
