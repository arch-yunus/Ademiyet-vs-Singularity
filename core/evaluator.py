from typing import List, Dict
from core.pillars import OntologyFirewall, CognitiveAirgap, FlawDefense

class AvSEvaluator:
    """The main engine for evaluating technologies against AvS-Core ethics."""
    
    def __init__(self):
        self.pillars = [
            OntologyFirewall(),
            CognitiveAirgap(),
            FlawDefense()
        ]

    def audit(self, proposal: Dict) -> Dict:
        """Runs a complete audit on a technology proposal."""
        results = []
        overall_score = 0
        
        for pillar in self.pillars:
            res = pillar.evaluate(proposal)
            results.append(res)
            overall_score += res["score"]
            
        final_score = overall_score / len(self.pillars)
        
        # Determine status based on score
        status = "REJECTED"
        if final_score > 85:
            status = "APPROVED"
        elif final_score > 60:
            status = "NEEDS REVISION"
            
        return {
            "proposal_name": proposal.get("name", "Unknown Technology"),
            "final_score": round(final_score, 2),
            "status": status,
            "detailed_results": results
        }
