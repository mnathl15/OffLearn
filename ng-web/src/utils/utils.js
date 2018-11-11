import { Constants } from "./constants";

export class Utils{

  static searchQuery(query){
      return this.getRequest(Constants.searchUrl + "=" + query);
  }

    static getRequest(url){
      return fetch(url)
          .then(function(response) {
            return response.json();
          })
          .then(function(myJson) {
            var json_string = JSON.stringify(myJson);
            console.log(json_string);
            return json_string;
          });
        }
      }
