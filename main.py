import json
import argparse
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from core.evaluator import AvSEvaluator

console = Console()

def print_banner():
    banner = """
    █████╗ ██╗   ██╗███████╗       ██████╗ ██████╗ ██████╗ ███████╗
    ██╔══██╗██║   ██║██╔════╝      ██╔════╝██╔═══██╗██╔══██╗██╔════╝
    ███████║██║   ██║███████╗█████╗██║     ██║   ██║██████╔╝█████╗  
    ██╔══██║╚██╗ ██╔╝╚════██║╚════╝██║     ██║   ██║██╔══██╗██╔════╝
    ██║  ██║ ╚████╔╝ ███████║      ╚██████╗╚██████╔╝██║  ██║███████╗
    ╚═╝  ╚═╝  ╚═══╝  ╚══════╝       ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
    [bold cyan]Ademiyet-vs-Singularity (AvS-Core) Bio-Ethics Evaluator[/bold cyan]
    """
    console.print(Panel(banner, border_style="bold magenta"))

def run_audit(file_path: str):
    evaluator = AvSEvaluator()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Evaluating bio-ethical integrity...", total=None)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                proposal = json.load(f)
        except Exception as e:
            console.print(f"[bold red]Error loading proposal:[/bold red] {e}")
            return

        report = evaluator.audit(proposal)
    
    # Header
    console.print(f"\n[bold yellow]Audit Report for:[/bold yellow] [bold white]{report['proposal_name']}[/bold white]")
    console.print(f"[bold yellow]Final Score:[/bold yellow] [bold]{report['final_score']}/100[/bold]")
    
    status_style = "bold green" if report["status"] == "APPROVED" else "bold red"
    if report["status"] == "NEEDS REVISION":
        status_style = "bold yellow"
    
    console.print(f"[bold yellow]Status:[/bold yellow] [{status_style}]{report['status']}[/{status_style}]\n")

    # Details Table
    table = Table(title="Pillar Evaluation Details", border_style="blue")
    table.add_column("Pillar", style="cyan")
    table.add_column("Score", justify="right")
    table.add_column("Issues/Findings", style="white")

    for res in report["detailed_results"]:
        issues_text = "\n".join(res["issues"]) if res["issues"] else "[green]No violations detected.[/green]"
        score_color = "green" if res["score"] > 80 else "yellow" if res["score"] > 50 else "red"
        table.add_row(res["pillar"], f"[{score_color}]{res['score']}[/{score_color}]", issues_text)

    console.print(table)
    console.print("\n[dim]AvS-Core: Witness to the digital age.[/dim]")

def main():
    parser = argparse.ArgumentParser(description="AvS-Core Evaluator")
    parser.add_argument("--audit", type=str, help="Path to the proposal JSON file")
    
    if len(sys.argv) == 1:
        print_banner()
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    
    if args.audit:
        print_banner()
        run_audit(args.audit)

if __name__ == "__main__":
    main()
