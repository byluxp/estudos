// Função para somar (a + b)
const somar = (a, b) => {
    return a + b;
};

// Função para subtrair (a - b)
const subtrair = (a, b) => {
    return a - b;
};

// Função para multiplicar (a * b)
const multiplicar = (a, b) => {
    return a * b;
};

// Função para dividir (a / b)
const dividir = (a, b) => {
    if (b === 0) {
        return "Erro: Divisão por zero";
    }
    return a / b;
};

// Função para potência (a elevado a b)
const exponencial = (a, b) => {
    return Math.pow(a, b);
};