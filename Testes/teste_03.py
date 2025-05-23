# 3 Teste Simples - Verificador de Palíndromo
def eh_palindromo(palavra):
    """Verifica se uma palavra é palíndromo (ignorando maiúsculas)"""
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

# Testes com print explicativo
print("--- TESTES MANUAIS ---")
print(f"'ovo' é palíndromo? {eh_palindromo('ovo')}")  # True
print(f"'python' é palíndromo? {eh_palindromo('python')}")  # False

# Testes automáticos com assert
print("\n--- TESTES AUTOMÁTICOS ---")
assert eh_palindromo("ana") == True, "Erro: 'ana' deveria ser True"
assert eh_palindromo("casa") == False, "Erro: 'casa' deveria ser False"
assert eh_palindromo("Ame a ema") == True, "Erro: Frase deveria ser True"

print("\n🎉 Todos os testes passaram! (Palíndromos verificados com sucesso)")
