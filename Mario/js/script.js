const mario = document.querySelector('.mario');
const pipe = document.querySelector('.pipe')
const clouds = document.querySelector('.clouds')
const canva = document.querySelector('.game-board')
canva.style.height = `${window.innerHeight}px`

const jump = () =>{
    mario.classList.add('jump');

    setTimeout( () => {
        mario.classList.remove('jump');
    } ,500)
}

document.addEventListener('keydown', jump);

const loop = setInterval(() => {
    const pipePosition = pipe.offsetLeft;
    const marioPosition = +window.getComputedStyle(mario).bottom.replace('px','');
    const cloudsPosition = +window.getComputedStyle(clouds).left.replace('px','');
    
    if (pipePosition <= 120 && marioPosition < 80 && pipePosition > 0)
    {
        pipe.style.animation = 'none';
        pipe.style.left=`${pipePosition}px`
        mario.style.animation = 'none';
        mario.style.bottom=`${marioPosition}px`

        mario.src = './images/game-over.png';
        mario.style.width = '75px';
        mario.style.marginLeft ='50px';

        clearInterval(loop)

        clouds.style.animation = 'none'
        clouds.style.left = `${cloudsPosition}px`
    }
}, 10);