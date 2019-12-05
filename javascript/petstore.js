
/**
 * This function should calculate the total amount of pet food that should be
 * ordered for the upcoming week.
 * @param numAnimals the number of animals in the store
 * @param avgFood the average amount of food (in kilograms) eaten by the animals
 * 				each week
 * @return the total amount of pet food that should be ordered for the upcoming
 * 				 week, or -1 if the numAnimals or avgFood are less than 0 or non-numeric
 */
function calculateFoodOrder(numAnimals, avgFood) {
    // IMPLEMENT THIS FUNCTION!
}

/**
 * Determines which day of the week had the most nnumber of people visiting the
 * pet store. If more than one day of the week has the same, highest amount of
 * traffic, an array containing the days (in any order) should be returned.
 * (ex. ["Wednesday", "Thursday"]). If the input is null or an empty array, the function
 * should return null.
 * @param week an array of Weekday objects
 * @return a string containing the name of the most popular day of the week if there is only one most popular day, and an array of the strings containing the names of the most popular days if there are more than one that are most popular
 */

function validateArray(simpleArray) {
    answer = false;
    if ((simpleArray !== undefined) && (simpleArray !== null)) { // array must be not null and not undefined
        if (simpleArray.length) {
            answer = true;
        } 
    }
    return answer
}

function mostPopularDays(week) { // @param week an array of Weekday objects
    // IMPLEMENT THIS FUNCTION!
    var answerArray = [];
    return answerArray;
}


/**
 * Given three arrays of equal length containing information about a list of
 * animals - where names[i], types[i], and breeds[i] all relate to a single
 * animal - return an array of Animal objects constructed from the provided
 * info.
 * @param names the array of animal names
 * @param types the array of animal types (ex. "Dog", "Cat", "Bird")
 * @param breeds the array of animal breeds
 * @return an array of Animal objects containing the animals' information, or an
 *         empty array if the array's lengths are unequal or zero, or if any array is null.
 */
function createAnimalObjects(names, types, breeds) {
    // IMPLEMENT THIS FUNCTION!
    var answerArray = [];
    // IMPLEMENT THIS FUNCTION!
    if (validateArray(names) && validateArray(types) &&  validateArray(breeds)) { // check if someone is null
        if ((names.length === types.length) && (breeds.length === types.length)) { // arrays with equal lenght 
            // this.__proto__ = new Animal()
            names.forEach((a, i) => {
                answerArray.push(new Animal(a, types[i], breeds[i]));
            }); // forEach

            // answerArray.push("ok");
        } else {
            console.log("not equal lengths");
        }
       
    } else {
        console.log("someone is null, undefined or length zero");
    }
    return answerArray
}

/////////////////////////////////////////////////////////////////
//
//  Do not change any code below here!
//
/////////////////////////////////////////////////////////////////


/**
 * A prototype to create Weekday objects
 */
function Weekday (name, traffic) {
    this.name = name;
    this.traffic = traffic;
}

/**
 * A prototype to create Item objects
 */
function Item (name, barcode, sellingPrice, buyingPrice) {
     this.name = name;
     this.barcode = barcode;
     this.sellingPrice = sellingPrice;
     this.buyingPrice = buyingPrice;
}
 /**
  * A prototype to create Animal objects
  */
function Animal (name, type, breed) {
    this.name = name;
     this.type = type;
     this.breed = breed;
}


/**
 * Use this function to test whether you are able to run JavaScript
 * from your browser's console.
 */
function helloworld() {
    return 'hello world!';
}

function testCreateAnimal() {
    names  = ["Peter", "Jessy", "Atlanta"]
    types  = ["Dog", "Cat", "Bird"]
    // breeds = null;
    // var breeds = [];
    // var breeds;
    breeds = ["Pug",  "Shorthair", "Tucan"]

    var arrayAnimalObjects = createAnimalObjects(names, types, breeds)
    if (validateArray(arrayAnimalObjects)) { // if array is not empty, or not undefined or not null, and with length
        console.log("answer ....");
        console.log(JSON.stringify(arrayAnimalObjects));     
    }  else {
        console.log("respuesta VACIA ....");   
    }
}


function testPopularDays() {
    var monday    = new Weekday("lunes", 5)
    var tuesday   = new Weekday("martes", 12);
    var wednesday = new Weekday("miércoles", 10);
    var thursday  = new Weekday("jueves", 14);
    var friday    = new Weekday("viernes", 18);
    var saturday  = new Weekday("sábado", 28);
    var sunday    = new Weekday("domingo", 32);

    var arrayOfWeekdayTestOne = {monday, tuesday, wednesday, thursday, friday, saturday, sunday}// array of week day objects 
    var answerOne = mostPopularDays(arrayOfWeekdayTestOne);
    if (answerOne) {
        console.log("answer, test one ............ ini");
        console.log(`answer must be: ${sunday.name} , ${sunday.traffic}`);
        console.log(answerOne);
        console.log("answer, test one ............ fin");
    }
    
}
