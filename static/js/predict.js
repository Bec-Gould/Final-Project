d3.select("#btn-predict").on("click", ()=>{
    // get values from html input fields 
    var age = d3.select("#age").node().value; 
    var gender = d3.select("#gender").node().value; 
    var state = d3.select("#state").node().value; 
    var offence = d3.select("#offence").node().value; 
    console.log(d3.select("#age").node().selectedOptions[0].innerHTML)
    console.log(d3.select("#gender").node().selectedOptions[0].innerHTML)
    console.log(d3.select("#state").node().selectedOptions[0].innerHTML)
    console.log(d3.select("#offence").node().selectedOptions[0].innerHTML)
    
    // perform a POST request using D3 
    d3.json("/api/predict", {
        // perform a POST request 
        method: "POST",
        // pass the following values in the 'body' of the POST request 
        body: JSON.stringify({
            "age": age,
            "gender": gender,
            "state": state,
            "offence": offence,
          }),
        // the headers contains metadata about the POST request. We want to say that the data sent is "json" data, so we set "Content-type": "application/json"
        headers: {
            "Content-type": "application/json"
        }
    }).then(response => { // when we receive the the response back, then we perform the steps below
        var prediction_output = d3.select("#prediction-output"); // select the area to put our predictions to
        console.log(response.prediction); // log out the result
        // if likely to be a victim
        if(response.prediction == 1){
            prediction_output.text("It is likely that you will be a victim of this crime."); 
        
        // if not likely to be a victim
        } else { 
            prediction_output.text("It is unlikely that you will be a victim of this crime.");
        }
    });
})