### run
Launch the code GUI

[source, python]
```python
{my_package}.run()
```

## How to build standalone exe for windows
NOTE: You must be on windows for that. (not sure if that's the case anymore)

Simply launch:
```bash
pyinstaller --onefile --noconsole run_{my_package}.py
```


