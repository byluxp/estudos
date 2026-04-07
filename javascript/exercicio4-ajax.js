function ajax(name,camada){ // recebe "nome" e coloca a informação na "camada" (local onde irá receber)
    var url = 'https:httpbin.org/get?text=' + name; // lembrar que var é VARIÁVEL, nesse caso eu defini a url
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() { // função que é chamada quando o estado da requisição muda
        if (this.readyState == 4 && this.status == 200) {
            var resp = xmlhttp.responseText;
            document.getElementById(camada).innerHTML = resp; // trocando a informação presente em "camada" e substituindo pela resp que eu defini ali em cima
        }
    };
    xmlhttp.open("GET", url, true); // método GET, url e true para assíncrono
    xmlhttp.send(); // envia a requisição para o servidor, nesse caso, a url definida acima
}