# 📌 Teste 01 - Verificação de soma 
def testar_soma():
    def somar(a, b):
        return a + b
    
    # Teste 1: Números positivos
    resultado = somar(2, 3)
    if resultado == 5:
        print("✅ Teste 1 passou: 2 + 3 = 5")
    else:
        print(f"❌ Falhou: 2 + 3 deveria ser 5, mas foi {resultado}")

    # Teste 2: Números negativos (caso extra)
    resultado = somar(-1, 1)
    if resultado == 0:
        print("✅ Teste 2 passou: -1 + 1 = 0")
    else:
        print(f"❌ Falhou: -1 + 1 deveria ser 0, mas foi {resultado}")

# Executar teste
testar_soma()
