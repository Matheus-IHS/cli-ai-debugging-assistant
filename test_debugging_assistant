# test_ai_service.py
from app import make_request_openai

def test_make_request_openai_com_sucesso(mocker):
    # 1. Criamos uma estrutura idêntica à resposta real da OpenAI
    mock_response = mocker.Mock()
    mock_choice = mocker.Mock()
    mock_choice.message.content = "Olá! Eu sou uma inteligência artificial simulada."
    mock_response.choices = [mock_choice]

    # 2. Substituímos o método 'create' da OpenAI para retornar a nossa resposta falsa
    mock_create = mocker.patch("app.OpenAI.chat.completions.create", return_value=mock_response)

    # 3. Executamos a nossa função normalmente
    resultado = make_request_openai("Quem é você?")

    # 4. Validações (Asserts)
    assert resultado == "Olá! Eu sou uma inteligência artificial simulada."
    
    # Garante que a API foi chamada com os parâmetros corretos
    mock_create.assert_called_once_with(
        model="gpt-5-nano",
        messages=[{"role": "user", "content": "Quem é você?"}]
    )
