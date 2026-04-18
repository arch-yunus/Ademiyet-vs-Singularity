from abc import ABC, abstractmethod
from typing import List, Dict

class Pillar(ABC):
    """Base class for Ademiyet-vs-Singularity ethical pillars."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def evaluate(self, proposal: Dict) -> Dict:
        """Evaluates a technology proposal against this pillar."""
        pass

class OntologyFirewall(Pillar):
    """
    1. Beşeriyet ile Ademiyet Ayrımı (The Ontology Firewall)
    Ensures human is not treated as a data-only modelable biological machine.
    """
    def __init__(self):
        super().__init__(
            "Ontology Firewall",
            "Beşeriyet ile Ademiyet ayrımını korur. İnsanı veri yığınına indirgeyen sistemleri denetler."
        )

    def evaluate(self, proposal: Dict) -> Dict:
        issues = []
        score = 100
        
        if proposal.get("models_emotions_as_data", False):
            issues.append("ERROR: Duygular ve vicdan veri olarak modellenemez (Ademiyet ihlali).")
            score -= 40
            
        if proposal.get("simulates_moral_judgment", False):
            issues.append("CRITICAL: Ahlaki kararların algoritmaya devredilmesi kabul edilemez.")
            score -= 50
            
        return {"pillar": self.name, "score": max(0, score), "issues": issues}

class CognitiveAirgap(Pillar):
    """
    2. Kognitif Bağımsızlık ve İrade (Cognitive Airgap)
    Ensures autonomy and prevents 'Hive Mind' integration.
    """
    def __init__(self):
        super().__init__(
            "Cognitive Airgap",
            "Zihinsel bağımsızlığı ve iradeyi korur. Bulut bağımlılığı ve kovan zihnini denetler."
        )

    def evaluate(self, proposal: Dict) -> Dict:
        issues = []
        score = 100
        
        if proposal.get("required_cloud_connection", False):
            issues.append("WARNING: Bireyin varoluşu bir sunucuya veya aboneliğe (Subscription Slavery) bağlanamaz.")
            score -= 30
            
        if proposal.get("external_will_override", False):
            issues.append("CRITICAL: İrade devri testi başarısız. Karar mekanizması dış manipülasyona açık.")
            score -= 60
            
        if proposal.get("hive_mind_integration", False):
            issues.append("CRITICAL: Kovan zihni (Hive Mind) hapsi; bireysel Ademiyetin sonudur.")
            score -= 70
            
        return {"pillar": self.name, "score": max(0, score), "issues": issues}

class FlawDefense(Pillar):
    """
    3. Zaaf ve Kusur Savunusu (Defense of Flaws)
    Protects human 'features' that are often labeled as 'bugs' by dataists.
    """
    def __init__(self):
        super().__init__(
            "Defense of Flaws",
            "İnsani kusurların (unutma, yorulma, acı çekme) birer 'feature' olduğunu savunur."
        )

    def evaluate(self, proposal: Dict) -> Dict:
        issues = []
        score = 100
        
        if proposal.get("removes_suffering_capability", False):
            issues.append("WARNING: Acı çekme yetisinin iptali, merhameti yok eder.")
            score -= 20
            
        if proposal.get("infinite_memory_override", False):
            issues.append("NOTE: Unutma yetisinin (hüzünle başa çıkma) devre dışı bırakılması fıtrata aykırıdır.")
            score -= 10
            
        if proposal.get("removes_fatigue", False):
            issues.append("NOTE: Yorulma yetisinin iptali, kanaat ve dengeyi bozar.")
            score -= 10

        return {"pillar": self.name, "score": max(0, score), "issues": issues}
