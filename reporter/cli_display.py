# reporter/cli_display.py

from rich.console import Console
from rich.table import Table

console = Console()

def display_file_result(file, findings, score):
    console.print(f"\n[bold cyan]Scanning:[/bold cyan] {file}")

    if findings:
        console.print("[bold yellow]Sensitive Data Found:[/bold yellow]")
        for label, matches in findings.items():
            console.print(f"  - [bold]{label}[/bold]: {len(matches)} instance(s)")

        if score >= 80:
            risk_level = "[red]High Risk[/red]"
        elif score >= 40:
            risk_level = "[yellow]Moderate Risk[/yellow]"
        else:
            risk_level = "[green]Low Risk[/green]"

        console.print(f"Risk Score: {score}/100 ({risk_level})")
    else:
        console.print("[green]No sensitive data found in this file.[/green]")

def display_summary(report_data):
    if not report_data:
        console.print("[green]No sensitive files found. Report not generated.[/green]")
        return

    table = Table(title="Data Leak Risk Summary")

    table.add_column("File", style="cyan", no_wrap=True)
    table.add_column("Risk Score", justify="center", style="magenta")
    table.add_column("Findings", style="yellow")

    for item in report_data:
        findings_summary = ", ".join(f"{k}: {len(v)}" for k, v in item["findings"].items())
        table.add_row(item["file"], str(item["score"]), findings_summary)

    console.print(table)
