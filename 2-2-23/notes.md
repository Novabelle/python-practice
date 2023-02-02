What if: Performing the operation "Copy Directory" on target "Item: C:\Users\SethHanslik\Programming\python-practice\2-9-23 Destination: C:\Users\SethHanslik\Programming\python-practice\2-23-23\2-9-23".
PS C:\Users\SethHanslik\Programming\python-practice> cp -WhatIf -Recurse -Path 2-9-23/* -Destination 2-23-23
What if: Performing the operation "Copy File" on target "Item: C:\Users\SethHanslik\Programming\python-practice\2-9-23\notes.md Destination: C:\Users\SethHanslik\Programming\python-practice\2-23-23\notes.md".
What if: Performing the operation "Copy File" on target "Item: C:\Users\SethHanslik\Programming\python-practice\2-9-23\practice.py Destination: C:\Users\SethHanslik\Programming\python-practice\2-23-23\practice.py".
What if: Performing the operation "Copy File" on target "Item: C:\Users\SethHanslik\Programming\python-practice\2-9-23\README.md Destination: C:\Users\SethHanslik\Programming\python-practice\2-23-23\README.md".
PS C:\Users\SethHanslik\Programming\python-practice> cp -Recurse -Path 2-9-23/* -Destination 2-23-23        
PS C:\Users\SethHanslik\Programming\python-practice> 


How do you run a python function?: python <file>

Sending stuff to github: 
1. `git status`
1. `git add <file>` 
1. or `git add <directory>`
1. `git status`
1. `git commit -m "what you did"`
1. `git push`