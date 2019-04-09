// Input: string of SMILES for a molecules
// Draws the molecule in the draw_mol canvas
// Returns nothing

var displayed_mol = '';
var displayed_mol_id = 0;

function draw_smiles(molecule, canvas) {
  let options = {
    width: 500,
    height: 500
  };
  //Initialize the drawer
  let smilesDrawer = new SmilesDrawer.Drawer(options);
  // Clean the input
  SmilesDrawer.parse(molecule, function(tree) {
  // Draw to the canvas
  smilesDrawer.draw(tree, canvas, 'light', false)
  });
};

function start_app() {
  document.getElementById('main').style.visibility='visible'
};

function remove_mol(score_id) {
  $.post('/remove',
  data={ 'score_id' : score_id },
  function(response, status) {
    location.reload();
  },
  dataType='json'
  )
}

function change_score(score_id) {
  $.post('/change_score',
  data={ 'score_id' : score_id },
  function(response, status) {
    location.reload();
  },
  dataType='json'
  )
}

$(document).ready(function(){

  // Get a random mol when starting the scoring.
  $.get('/get_mol_not_scored',
  function(response) {
    // Update the molecule id everytime a new molecule is displayed
    displayed_mol = response['smiles']
    displayed_mol_id = response['id']
    draw_smiles(response['smiles'], 'draw_mol')
  });

  // Select synthesisable button
  $('#score-yes').click(function() {
    $.post('/score', // Remember to send the currently displayed mols id in order to score the previous mol, then can get a new one
    {'score' : 1, 'id' : displayed_mol_id},
    function(response, status) {
      displayed_mol = response['smiles']
      displayed_mol_id = response['id']
      draw_smiles(response['smiles'], 'draw_mol')
    },
    dataType='json'
    )
  });

  // Select unsynthesisable button
  $('#score-no').click(function() {
    $.post('/score',
    data={ 'score' : 0,
           'id' : displayed_mol_id },
    function(response, status) {
      displayed_mol = response['smiles']
      displayed_mol_id = response['id']
      draw_smiles(response['smiles'], 'draw_mol')
    },
    dataType='json'
    )
  });

  // Select unsure button
  $('#score-unsure').click(function() {
    $.post('/score',
    data={ 'score' : 2,
           'id' : displayed_mol_id },
    function(response, status) {
      displayed_mol = response['smiles']
      displayed_mol_id = response['id']
      draw_smiles(response['smiles'], 'draw_mol')
    },
    dataType='json'
    )
  });

});
