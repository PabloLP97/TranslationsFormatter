# TranslationsFormatter
## Instalation
<pre>pip3 install -r requirements.txt</pre>

## Usage
Use <pre>python3 main.py file_name.xlsx</pre> or <pre>python3 main.py file_name.xlsx prefix</pre>
### Where
__file_name.xlsx__ is the excel file to format

__prefix__ is the prefix text to check (and replaces default value when passed)


## Extra: easy use with alias
### Add new alias
Edit the file __~/.zshrc__

Add a new alias with your favourite name
<pre>alias translations='python3 /Full/Path/to/main.py $1</pre>
Example
<pre>alias tradus='python3 /Users/pablolp/Documents/GitHub/TranslationsFormatter/main.py $1'</pre>

### Use the alias
Then restart the console, type the alias and drop the file to format in to the terminal window.
<pre>translations /Full/Path/to/excel.xlsx</pre>
Example
<pre>tradus /Users/pablolp/Downloads/Traducciones.xlsx</pre>

