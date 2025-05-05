const NON_LIST_PLACE_DATA_FORM_LABELS = ["name", "rating", "tagline", "city", "country"]
const LIST_PLACE_DATA_FORM_LABELS = ["types", "coordinates"];
const REVIEW_FORM_LABELS = ["name", "review"]

window.addEventListener('load', function () {
    const review_button = document.getElementById("review-form-submit-button");
    const reviewForm = document.getElementById("review-form");
    const reviewFormElements = document.getElementById("review-form").elements;

    populatePlaceDataFormElements(reviewFormElements)
    populatePlaceReviewFormElements(reviewFormElements)

    review_button.addEventListener("click", async function () {

        responseCode = await executeRequest(reviewFormElements);

        if (responseCode == "200") {
            reviewForm.append("Review post suceeded");
            reviewForm.reset();
        } else {
            reviewForm.append("Review post failed");
        }
    });
  })

function executeRequest(formElements) {
    var data = {}
    const placeDataPayload = getPlaceDataPayload(formElements)
    const placeReviewPayload = getPlaceReviewPayload(formElements)

    data['place_data'] = placeDataPayload
    data['place_review'] = placeReviewPayload

    const jsonPayload = JSON.stringify(data);

    const responseStatus = fetch('/place', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: jsonPayload
      })
      .then(response => response.status)
    
      return responseStatus
}

function getPlaceDataPayload(formElements) {
    const placeDataPayload = {}
    NON_LIST_PLACE_DATA_FORM_LABELS.forEach(inputName => addInputToPayload(placeDataPayload, inputName, false, formElements))
    LIST_PLACE_DATA_FORM_LABELS.forEach(inputName => addInputToPayload(placeDataPayload, inputName, true, formElements))
    return placeDataPayload
}

function getPlaceReviewPayload(formElements) {
    const placeReviewPayload = {}
    REVIEW_FORM_LABELS.forEach((inputName => addInputToPayload(placeReviewPayload, inputName, false, formElements)))
    return placeReviewPayload
}

function addInputToPayload(payload, inputName, isListInput, formElements) {
    var input = formElements[inputName].value;
    if (input) {
        if (isListInput) {
            input = input.split(", ")
        }
        payload[inputName] = input
    }
}

function populatePlaceDataFormElements(formElements) {
    try {
        if (existingPlaceData) {
            NON_LIST_PLACE_DATA_FORM_LABELS.forEach(input => populateFormField(existingPlaceData, input, false, formElements));
            LIST_PLACE_DATA_FORM_LABELS.forEach(input => populateFormField(existingPlaceData, input, true, formElements));
        }
    } catch (ReferenceError) {}
}

function populatePlaceReviewFormElements(formElements) {
    try {
        if (existingPlaceReview) {
            REVIEW_FORM_LABELS.forEach(input => populateFormField(existingPlaceReview, input, false, formElements));
        }
    } catch (ReferenceError) {}
}

function populateFormField(existingData, inputName, isListInput, formElements) {
    var existingInput = existingData[inputName];
    if (existingInput) {
        if (isListInput) {
            existingInput = existingInput.join(", ");
        }
        formElements[inputName].value = existingInput;
    }
}
