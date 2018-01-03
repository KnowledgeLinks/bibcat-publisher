import React from "react";
import SearchResults from "./Search";
import NavigationBar from "./Navigation";

/*function Search(props) {
    return (
        <form className="form-inline mx-lg-3" method="POST" action="{props.action}">
            <div className="form-group">
                <input className="form-control" id="query" placeholder="Query"></input>
            </div>
            <button type="submit" className="btn btn-primary">Search</button>
        </form>
    );
}*/

export default class App extends React.Component {
    render () {
        return (
            <div className="container">
                <NavigationBar />
                <SearchResults results={RESULTS} />
            </div>
        );
    }
}

const RESULTS = [
    { title: "Colorado state Workforce Investment Act plan modification for program year 2009",
      thumbnail: "http://hermes.cde.state.co.us/drupal/islandora/object/co%3A1002/datastream/PREVIEW/view",
      author: "None",
      summary: "Colorado state WIA plan modification for program year 2009" },
    { title: "Test Video",
      thumbnail: "",
      author: "Doe, Jane",
      summary: "This is a sample summary" }
];
