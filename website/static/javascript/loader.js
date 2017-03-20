function showLoader(evt)
{ 
    var loader_button = evt.target;
    
    document.getElementById(loader_button.id).style.display = 'none';

    var loader = document.getElementById(loader_button.id + '_loader');
    loader.style.display = 'table';
    loader.style.visibility = 'visible';
}

function hideLoader(loader_button_id)
{
    document.getElementById(loader_button_id).style.display = 'block';

    var loader = document.getElementById(loader_button_id + '_loader');
    loader.style.display = 'none';
    loader.style.visibility = 'hidden';
}

// Add event listeners
var loader_buttons = document.getElementsByClassName('button_with_loader');

for (var i=0; i<loader_buttons.length; i++)
{
    loader_buttons[i].addEventListener('click', function(event) { showLoader(event) } );
}
