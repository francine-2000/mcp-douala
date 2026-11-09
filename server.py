from mcp.server.fastmcp import FastMCP


mcp = FastMCP("mcp-douala")


@mcp.tool()
def salut_douala(nom: str) -> str:
    """Salue une personne depuis Douala."""
    return f"Salut {nom} depuis Douala !"


@mcp.tool()
def fcfa_en_euro(montant: float) -> float:
    """Convertit un montant en FCFA en euros au taux fixe de 656 FCFA par euro."""
    return montant / 656


if __name__ == "__main__":
    mcp.run()
