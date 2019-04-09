var og = 0;
    var fg = 0;
    var abv = document.getElementById('id_abv');
    var ogField = document.getElementById('id_original_gravity_sg');
    var fgField = document.getElementById('id_final_gravity_sg');
    var platoOG = document.getElementById('id_original_gravity_plato');
    var platoFG = document.getElementById('id_final_gravity_plato');
    platoOG.addEventListener('input', function(){
        og = ((platoOG.value) / (258.6 - (platoOG.value / 258.2 * 227.1))) + 1;
        fg = ((platoFG.value) / (258.6 - (platoFG.value / 258.2 * 227.1))) + 1;
        abv.value = Math.round(((og - fg) * 131.25) * 100) / 100;
    });

    platoFG.addEventListener('input', function(){
        og = ((platoOG.value) / (258.6 - (platoOG.value / 258.2 * 227.1))) + 1;
        fg = ((platoFG.value) / (258.6 - (platoFG.value / 258.2 * 227.1))) + 1;
        abv.value = Math.round(((og - fg) * 131.25) * 100) / 100;
    });

    ogField.addEventListener('input', function(){
        og = ogField.value;
        fg = fgField.value;
        abv.value = Math.round(((og - fg) * 131.25) * 100) / 100;
    });

    fgField.addEventListener('input', function(){
        og = ogField.value;
        fg = fgField.value;
        document.getElementById('id_abv').value = Math.round(((og - fg) * 131.25) * 100) / 100;
    });

    var hopBlock = document.getElementById('hop-block');
    var wrapper = document.getElementsByTagName('form');
    var hiddenInput = document.createElement('input');
    hiddenInput.style.display = 'none';
    hopBlock.before(hiddenInput)
    hiddenInput.id = 'id_hidden';
    hiddenInput.name = 'hop-counter';
    var hopCounter = 0;
    var btn = document.getElementById('add-hop');
    btn.addEventListener('click', function(event){
        event.preventDefault();
        hopCounter++;
        hiddenInput.value = hopCounter;
        var cln = hopBlock.cloneNode(true);

        //Modifies the ids and names of children of cloned div.
        for (let child of cln.children) {
            child.children[1].name = child.children[1].name + '_' + hopCounter;
            child.children[1].id = child.children[1].id + '_' + hopCounter;
        }
        cln.id = cln.id + '_' + hopCounter;
        console.log(cln.children[0].children[1].id , cln.children[1].children[1].id , cln.children[2].children[1].id);

        btn.before(cln);
    });

//Gravity selector buttons, show only selected inputs//
    var plato = document.getElementById('plato');
    var sg = document.getElementById('sg');


    function switchToPlato(){
            ogField.style.display = 'none';
            ogField.previousSibling.style.display = 'none';
            fgField.style.display = 'none';
            fgField.previousSibling.style.display = 'none';
            platoFG.style.display = 'block';
            platoFG.previousSibling.style.display = 'block';
            platoOG.previousSibling.style.display = 'block';
            platoOG.style.display = 'block';
            plato.checked = 'true';
        };
    function switchToSg(){
            platoFG.style.display = 'none';
            platoFG.previousSibling.style.display = 'none';
            platoOG.previousSibling.style.display = 'none';
            platoOG.style.display = 'none';
            ogField.style.display = '';
            ogField.previousSibling.style.display = '';
            fgField.style.display = '';
            fgField.previousSibling.style.display = '';
        }

    switchToPlato();



    plato.addEventListener('click', switchToPlato)
    sg.addEventListener('click', switchToSg )
