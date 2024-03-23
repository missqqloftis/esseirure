from rich.console import Console

console = Console()

def cprint(text, color="white"):
    console.print(text, style=f"bold {color}")

cprint(f'\n>>> HOP swap | {error}', 'red')
