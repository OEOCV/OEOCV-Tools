Paste the configuration below into config.cson (be sure to install the atom-shell-commands package and https://github.com/Bridgeconn/usfm-grammar). `check-format-short` requires single-validate to be copied into `/usr/local/bin`.

```
"atom-shell-commands":
  commands: [
    {
      name: "check-format"
      command: "usfm-grammar"
      arguments: [
        "{FileName}"
      ]
      options:
        cwd: "{FileDir}"
        keymap: "ctrl-4"
        save: true
    },
    {
      name: "check-format-short"
      command: "/usr/local/bin/single-validate.sh"
      arguments: [
        "{FilePath}"
      ]
      options:
        cwd: "{FileDir}"
        keymap: "ctrl-2"
        save: true
    }
  ]
```
