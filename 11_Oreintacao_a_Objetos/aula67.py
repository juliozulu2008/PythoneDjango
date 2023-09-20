"""
Metodo pythoniano de fazer gettes e setter
"""
"""
Ao  fazer um getter e setter com um atribulto privado o pythom me retornou um erro
de recursao infinita, ao pesquisar descobri que é porque nao se usar getter e setter em 
atributos publicos sempre privados ou Proptegidos, se nao vira redundancia
"""


class Professor:
    def __init__(self, nome, idade, disciplina):
        self._nome = nome
        self._idade = idade
        self._disciplina = disciplina

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        self._idade = nova_idade

    @property
    def disciplina(self):
        return self._disciplina

    @disciplina.setter
    def disciplina(self, nova_disciplina):
        self._disciplina = nova_disciplina


prof1 = Professor("Joao", 38, "Matematica")
print(prof1.nome)
print(prof1.idade)
print(prof1.disciplina)
