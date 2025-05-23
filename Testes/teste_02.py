#  Teste 2 - Verificador de Números Pares/Ímpares
# Objetivo: Criar uma função que classifica números e testar sua precisão

def classificar_numero(numero):
    """Classifica um número como Par, Ímpar ou Zero"""
    if numero == 0:
        return "Zero"
    elif numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Testes manuais (com prints explicativos)
print("--- TESTES MANUAIS ---")
print(f"5 é {classificar_numero(5)}")      # Deve retornar "Ímpar"
print(f"8 é {classificar_numero(8)}")      # Deve retornar "Par"
print(f"0 é {classificar_numero(0)}")      # Deve retornar "Zero"

# Testes automáticos (com asserts)
print("\n--- TESTES AUTOMÁTICOS ---")
assert classificar_numero(2) == "Par", "Erro: 2 deveria ser Par"
assert classificar_numero(7) == "Ímpar", "Erro: 7 deveria ser Ímpar"
assert classificar_numero(0) == "Zero", "Erro: 0 deveria ser Zero"

print("\n🎉 Todos os testes passaram com sucesso!")
