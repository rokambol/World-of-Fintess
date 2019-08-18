{"filter":false,"title":"models.py","tooltip":"/accounts/models.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":12,"column":33},"action":"insert","lines":["from django.db import models","from django.contrib.auth.models import User","","# Create your models here - ACCOUNTS.","","","class Swimmer(models.Model):","    user = models.OneToOneField(User, on_delete=models.CASCADE,","                                related_name='swimmer')","    graduation_year = models.CharField(max_length=5)","","    def __str__(self):","        return self.user.username"],"id":1}],[{"start":{"row":3,"column":26},"end":{"row":3,"column":37},"action":"remove","lines":["- ACCOUNTS."],"id":2}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"remove","lines":["r"],"id":3},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"remove","lines":["e"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"remove","lines":["m"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"remove","lines":["m"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"remove","lines":["i"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"remove","lines":["w"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"remove","lines":["S"]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["U"],"id":4},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["s"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["e"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"remove","lines":["r"],"id":5},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"remove","lines":["e"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"remove","lines":["s"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"remove","lines":["U"]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["F"],"id":6},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["i"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["t"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["e"],"id":7},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["s"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["U"],"id":8},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["s"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["e"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"remove","lines":["graduation_year = models.CharField(max_length=5)",""],"id":9}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":33},"end":{"row":11,"column":33},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566163739725,"hash":"c4b828f14b38d6b5fe4ae3c5d64a0d40659fe450"}