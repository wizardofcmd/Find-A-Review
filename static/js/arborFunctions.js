function loadcanvas() {
  var canvas = document.createElement('canvas');
  var div = document.getElementById('arbor');
  canvas.id = "viewport";
  canvas.width = "1000";
  canvas.height = "688";
  canvas.class = "modal-content"
  div.appendChild(canvas);
}

function createcanvas() {
  var canvas = document.createElement('canvas');
  var div = document.getElementById('arbor');
  canvas.id = "viewport";
  canvas.width = "0";
  canvas.height = "0";
  canvas.class = "modal-content"
  div.appendChild(canvas);
}

function insertData(){
  var sys = arbor.ParticleSystem(1000, 400, 1);
  sys.parameters({
    gravity: true
  });
  sys.renderer = Renderer("#viewport");
  var sentiment;
  var sentiment_col, negcolor, poscolor;


  var neg, neu, pos, compound;
  $.getJSON('/analysis', function(data) {

    sentiment = data.sentiment;
    neg = JSON.stringify(data.points.neg);
    neu = JSON.stringify(data.points.neu);
    pos = JSON.stringify(data.points.pos);
    compound = JSON.stringify(data.points.compound);


  if(neg <= '0.5'){
    negcolor = "#e7070780";
  } else if ( neg > '0.5' ){
     negcolor = "#e70707";
  }
  if(pos <= '0.5'){
     poscolor = "#9ce62a80";
  } else if ( pos > '0.5' ){
     poscolor = "#9ce62a";
  }



    if(sentiment == 'positive'){
      sentiment_col = "#9ce62a";
  }else if (sentiment == 'negative'){
      sentiment_col = "#e70707"
    }
    else{
        sentiment_col = "#f58742"
    }
    console.log(JSON.stringify("sentiment= "+sentiment));
    console.log(JSON.stringify("neg= "+neg));
    console.log(JSON.stringify("neu= "+neu));
    console.log(JSON.stringify("pos= "+pos));
    console.log(JSON.stringify("compound= "+compound));
    var b_data = {
      nodes: {},
      edges: {
        genre: {}
      }
    };

    var genre = {
      genre: {
        label: "Sentiment:",
        sentiment: sentiment,
        shape: "dot",
        color: sentiment_col
      }
    };

    var edges = {
      genre: {}
    };
    var nodes = {};
    //console.log(pos);
    edges['genre']['Negative'] = {};
    edges['genre']['Neutral'] = {};
    edges['genre']['Positive'] = {};
    edges['genre']['Compound'] = {};

    nodes['Negative'] = {};
    nodes['Neutral'] = {};
    nodes['Positive'] = {};
    nodes['Compound'] = {};

    nodes['Negative'].label = "Negativity:";
    nodes['Negative'].neg = neg;
    nodes['Negative'].shape = "dot";
    nodes['Negative'].color = negcolor;

    nodes['Neutral'].label = "Neutrality:";
    nodes['Neutral'].neu = neu;
    nodes['Neutral'].shape = "dot";

    nodes['Positive'].label = "Positivity:";
    nodes['Positive'].pos = pos;
    nodes['Positive'].shape = "dot";
    nodes['Positive'].color = poscolor;

    nodes['Compound'].label = "Compound:";
    nodes['Compound'].compound = compound;
    nodes['Compound'].shape = "dot";
    nodes['Compound'].color="yellow";

    Object.assign(b_data.nodes, nodes);
    Object.assign(b_data.edges, edges);
    Object.assign(b_data.nodes, genre);

    console.log(b_data);
    sys.graft(b_data);
  }).fail(function() {
    console.log("No data has been submitted");
  });

}
function absolutelyDestroyCanvas() {
  var elem = document.getElementById("viewport");
  elem.parentNode.removeChild(elem);
}
