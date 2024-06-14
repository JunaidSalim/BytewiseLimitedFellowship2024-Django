## Mediun Article:
https://medium.com/@junaidsaleem986/basic-powershell-commands-a1a05435b7ea

## Some common keyboard shortcuts or keybindings:
```markdown

Before we look at some common commands, I just want to note a few keyboard commands that are very helpful:

- Up Arrow: Will show your last command
- Down Arrow: Will show your next command
- Tab: Will auto-complete your command
- Ctrl + L: Will clear the screen
- Ctrl + C: Will cancel a command
- Ctrl + R: Will search for a command

```

## The `whoami` Command

The `whoami` command will show you the current user that you are logged in as.

```bash
whoami
```

---

## The `date` Command

Another really simple one is the `date` command, which, surprise, will show you the current date and time.

```bash
date
```

---

## The `pwd` Command

The `pwd` command will show you the current working directory you are in.

```bash
pwd
```

---

## The `mkdir` Command

The `mkdir` command is used to create a new directory. You can specify the name of the directory you want to create, and `mkdir` will create it in the current working directory. If you provide a path, it will create the directory at the specified location. This command is useful for organizing files and directories into a structured hierarchy.

```bash
mkdir directory_name
```

### Arguments and Flags

- **Directory Name**: The primary argument is the name of the directory you want to create.

### Common Flags

- `-p` or `--parents`: Creates the parent directories if they do not exist. This is useful for creating nested directories in one command.

    ```bash
    mkdir -p /path/to/new/directory
    ```

---

## The `touch` Command

The `touch` command is used to create an empty file or update the access and modification timestamps of an existing file. It is commonly used to quickly create new, empty files.

```bash
touch filename
```

### Arguments and Flags

- **File Name**: The primary argument is the name of the file you want to create or update.

### Common Flags

- `-a`: Changes the access time of the file only. This is useful if you only want to update when the file was last accessed without modifying the modification time.

    ```bash
    touch -a file.txt
    ```

- `-m`: Changes the modification time of the file only. This is useful if you only want to update when the file was last modified without changing the access time.

    ```bash
    touch -m file.txt
    ```

- `-c` or `--no-create`: Does not create the file if it does not exist. This is useful if you only want to update timestamps of existing files and avoid creating new ones accidentally.

    ```bash
    touch -c file.txt
    ```

---

## The `rm` Command

The `rm` command is used to remove files or directories. You can specify the name of the file or directory you want to delete, and `rm` will remove it from the file system. This command is useful for cleaning up unwanted files and directories.

```bash
rm filename
```

---

## The `cp` Command

The `cp` command is used to copy files or directories from one location to another. You can specify the source file or directory and the destination where you want the copy to be placed. This command is useful for duplicating files and directories.

```bash
cp source_file destination_file
```

---

## The `mv` Command

The `mv` command is used to move or rename files or directories. You can specify the source file or directory and the destination path or new name. This command is useful for organizing and renaming files and directories.

```bash
mv old_name new_name
```

---

## The `cat` Command

The `cat` command is used to concatenate and display the contents of files. You can specify one or more files, and `cat` will print their contents to the standard output. This command is useful for viewing the contents of files quickly.

```bash
cat filename
```

---

## The `head` Command

The `head` command is used to display the first few lines of a file. By default, it shows the first 10 lines. You can specify a different number of lines using the `-n` option. This command is useful for previewing the beginning of files.

```bash
head filename
```

---

## The `tail` Command

The `tail` command is used to display the last few lines of a file. By default, it shows the last 10 lines. You can specify a different number of lines using the `-n` option. This command is useful for viewing the end of files, especially for log files.

```bash
tail filename
```

---

## The `echo` Command

The `echo` command is used to display text or a variable's value on the terminal or console. It is commonly used in shell scripting and command-line operations to output information to the user or as part of a script's output.

### Syntax

```bash
echo [options] [text or variable]
```

### Options

- `-e`: Enables interpretation of backslash escapes, allowing special characters like newline (`\n`) to be interpreted.

    ```bash
    echo -e "Hello\nWorld"
    ```

- `-n`: Suppresses the trailing newline, so the output does not include a newline character at the end.

    ```bash
    echo -n "This is a message "
    echo "without a newline."
    ```

```markdown
The `echo` command is versatile and can be used in various ways to output text or variable values in shell scripts and command-line operations.
```
