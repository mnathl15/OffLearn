import { Constants } from "./constants";

export class Utils{

    static searchQuery(query){
        return this.getRequest(Constants.searchUrl + "=" + query);
    }

    static getRequest(url){
        console.log(url);
        
        fetch(url)
            .then(response => response.json())
            .then(function(data){
                return data
            })
    }
}