# worpi
A prototype of a private Swiss Army knife for easier handling of folders, files and their creation, also includes a task list, etc. 
Everything that makes my work more pleasant or can be more enjoyable.
...
This program fits my work ergonomics, so it may not suit everyone. And I emphasize: it's a prototype in development. It makes it easier for me to create folders and files, creates a list of updated files so that I know what to store on the cloud or external drive (despite the fact that I also use git) I save system resources and time, 
because this way of versioning is much easier than git )), contains a task list, watches over my time at the computer (if I want to). 
Expanding this program does not set limits, because it is primarily designed to improve the ergonomics of my work.

Example of working in the system:
Establishing a new project:
1. creates a folder in the directory I specify
2. creates a new file in the created folder after entering its name and extension
3. automatically creates a b version of the created file, thanks to which it then creates a report of changes 
that I made in the master file, then creates a file in which the history of changes based on the b file and a file 
for writing project documentation is stored.

Second example:
Edit any file:
1. enter the address of the parent folder in which the project folder is located
2. the program will offer me a numerically indexed list of all subfolders of the parent folder (then it is easier for me to switch to the specified subfolder (I do not have to write the address))
3. I choose the folder number and enter it into the program
4. the program will offer me a numerically indexed list of files that the folder contains
5. I enter the number of the file into the program and nano opens automatically and I can edit
6. After saving the changes, the program automatically detects what I have edited and records this information in the change history file.

The program is not in the English version, because I do not assume that anyone will be interested in it, 
even if only for inspiration (so why would I bother :-))
