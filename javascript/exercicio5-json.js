const url = 'https://randomuser.me/api/?results=10';

async function getUsers(lista) { // função pegar users da lista (Estou criando a função)
    const resp = await fetch(url); // pede a resposta da API
    const objeto = await resp.json(); // espera a resposta e converte para JSON
    let itens = '';
     for (let pessoa of objeto.results) { // para cada pessoa do array results
        itens += `<li>${pessoa.name.first} ${pessoa.name.last}</li>`; // adiciona primeiro e ultimo nome em forma de lista
        }
    document.getElementById(lista).innerHTML = itens; // sunstitui as infos da lista pelos itens no html
}