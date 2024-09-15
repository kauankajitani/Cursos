const nome = 'Luiz Otávio';
const sobrenome = 'Miranda'
const idade = 30;
const peso = 84;
const alturaEmCm = 1.80;
let anoNascimento = 2022 - idade;
let imc = peso/(alturaEmCm*alturaEmCm);

console.log(`${nome} ${sobrenome} tem ${idade} anos pesa ${peso} kg tem ${alturaEmCm} de altura e seu IMC é de ${imc}`);
console.log(`${nome} nasceu em ${anoNascimento}`)