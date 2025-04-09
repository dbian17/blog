window.addEventListener('load', function () {


    

    review_button.addEventListener("click", async function () {

        responseCode = await executeRequest(reviewFormElements);

        if (responseCode == "200") {
            reviewForm.append("Review post suceeded");
        } else {
            reviewForm.append("Review post failed");
        }
    });
  })

function executeRequest(formElements) {

}

