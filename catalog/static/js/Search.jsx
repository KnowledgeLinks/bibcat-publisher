import React from "react";
var $ = require("jquery");

export default class Search extends React.Component {

    constructor(props) {
        super(props);
        this.state = {"queryTerms": []};
        this.handleQuery = this.handleQuery.bind(this);
        this.queryServer = this.queryServer.bind(this);
    }

    handleQuery(event) {
        this.setState({"queryTerms": event.target.value});

    }

    queryServer(event) {
        // Query bibcat search api
        var params = { body: {query: this.state.queryTerms},
                       method: "POST" };
        fetch('search', params).then(function(response) {
            alert("Response from server is " + response.results + " for " + response.query);
        });
        
        event.preventDefault();
    }

    render () {
        return (
            <form className="form-inline mx-lg-3" onSubmit={this.queryServer}>
                <div className="form-group">
                    <input className="form-control" 
                           id="query" 
                           value={this.state.queryTerms}
                           onChange={this.handleQuery}
                           placeholder="Query"></input>
                </div>
                <button type="submit" className="btn btn-primary">Search</button>
            </form>
        );
    }
}
