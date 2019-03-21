
let correct = 0;
let question_number = 0;

let total_ques = 0

document.addEventListener("DOMContentLoaded",()=>{	fetch_data();  });

function fetch_data(){
    $.ajax({
        url : '/question/'+question_number,
        success : function(data){ load_question(data); }, });
 	}


function load_question(data) { 
	if ( data ) {
		
		if (!total_ques){
		set_question_buttons(data);
		}
		
		document.querySelector("#question").innerHTML = "Q."+(question_number+1)+" "+ data.question;
		const options = document.querySelector("#options");
		options.innerHTML = "";
		
		for ( const option of data.options){
			options.innerHTML += `<button class="option">${option}</button><br>`; }; 

			document.querySelectorAll(".option").forEach(option => {
				option.onclick = (b) => { 
						var ans = option.textContent;
						
                        $.ajax({
                            url : '/check_question/',
                            type : 'POST',
                            data : { ques:question_number,answer:ans },
                            success : function(data){
                            
								if (data){ correct += 1; } 
							document.querySelectorAll("#question_b")[question_number].style.background = 'green';
							question_number += 1;
							if ( question_number < total_ques ){
							document.querySelectorAll("#question_b")[question_number].style.background = 'gray';
							document.querySelector("#correct").innerHTML = correct+" of "+question_number;
							}; 
							
						fetch_data();
                            }
                        })
					}
					})
					}

				else {
						document.querySelector("#question").innerHTML = "Congratulations You Have Completed Python Quiz";
						document.querySelector("#options").innerHTML = "";
						document.querySelector("#result").innerHTML = "Your Final Score is : "+correct+"/"+question_number;
						}
					};


function set_question_buttons(data) {
		total_ques = data.total_questions
		document.querySelector("#total_ques").innerHTML = data.total_questions;
		let s = ""
		for (var i=0;i<total_ques;i++){
		s+="<button id=question_b>"+(i+1)+"</button>";	
		}
		document.querySelector("#question_button").innerHTML = s;
		document.querySelectorAll("#question_b")[question_number].style.background = 'gray';
		document.querySelectorAll("#question_b").forEach( function(button) {
			button.addEventListener("click",function(){	
			document.querySelectorAll("#question_b")[question_number].style.background = "#e7e7e7";
			this.style.background = 'gray';  	
			question_number= button.textContent - 1;
			fetch_data();
			})
		})
	}