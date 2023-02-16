const adj = ["Flowery", "Macho", "Pretty", "Tall", "Short", "Pink", "Purple", "Flashy", "Goofy", "Wizard", "Cool", "Artsy"];
const noun = ["Men", "Women", "Girls", "Boys", "Cats", "Dogs", "Kids", "Bands", "Gang", "Skaters", "Gamers", "Puppies", "Moms", "Dads", "Sisters", "Brothers"];


let generateName = () => {
    let fName = adj[Math.floor(Math.random() * adj.length)];
    let lName = noun[Math.floor(Math.random() * noun.length)];

    return `Your random group name: ${fName} ${lName}!`;
}

console.log(generateName());