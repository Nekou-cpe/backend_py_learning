let score=JSON.parse(localStorage.getItem('score'));
let youchose='';

function random(){
    const randomNumber=Math.random();
    let code='';
    if (randomNumber>=0 && randomNumber<1/3){
        code='Rock';
    }
    else if(randomNumber>=1/3 && randomNumber<2/3){
        code='Papper';
    }
    else{
        code='Sissors';
    }
    return code;
}
function playGame(youchose){            
    let codeRandom=random();
    let result='';
    if ((youchose===codeRandom)){
        result='tie';
    }
    else if (((youchose==='Papper')&&(codeRandom==='Rock'))||((youchose==='Sissors')&&(codeRandom==='Papper'))||(youchose=='Rock' && codeRandom=='Sissors')){
        result='you win';
    }
    else if (youchose==='reset'){
        score={
            wins:0,
            loses:0,
            ties:0
        };
        result='reset';
    }
    else {
        result='you lose';
    }
    if(result==='tie'){score.ties+=1;}
    else if(result==='you win'){score.wins+=1;}
    else if (result==='reset'){score.ties=0;score.wins=0;score.loses=0;}
    else{score.loses+=1;}

    localStorage.setItem('score',JSON.stringify(score));
    if (result==='reset'){
        alert(`rested game
            wins:${score.wins}
            loses:${score.loses}
            ties:${score.ties}`);
    }
    else{
        alert(`code choses ${codeRandom} so ${result} 
            wins:${score.wins}
            loses:${score.loses}
            ties:${score.ties}`); 
    }

}