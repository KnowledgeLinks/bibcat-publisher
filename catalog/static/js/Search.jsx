import React from "react";
var $ = require("jquery");


class ResultsMediaList extends React.Component {
    render () {
        const searchResults = [];
        this.props.results.forEach((result) => 
        {
            searchResults.push(
                <ResultMediaObject 
                    thumbnail={result.thumbnail}
                    title={result.title}
                    author={result.author} 
                    summary={result.summary}/>    
            );

        });
        return (
            <ul class="list-unstyled">
            {searchResults}
            </ul>
        );
    }
}

class ResultMediaObject extends React.Component {

    render () {
        return (
            <li class="media">
            <img class="mr-3" width="150px" height="300px" src={this.props.thumbnail} alt={this.props.title} />
            <div class="media-body">
                <h5 class="mt-0 mb-1">{this.props.title} by {this.props.author}</h5>
                {this.props.summary}
            </div>
        </li>
        );
    }
}

class SearchBar extends React.Component {

    /*constructor(props) {
        super(props);
        this.state = {"queryTerms": [], "size": 0};
        this.handleQuery = this.handleQuery.bind(this);
        this.queryServer = this.queryServer.bind(this);
    }

    handleQuery(event) {
        this.setState({"queryTerms": event.target.value});

    }

    queryServer(event) {
        // Query bibcat search api
        var params = { query: this.state.queryTerms}
        $.ajax({
            type: "POST",
            url: "search",
            data: params,
            success: function(res) {
                this.setState({"size": res.results.length}) 
            }.bind(this)
        });
        
        event.preventDefault();
    } */

    render () {
        return (
            <form className="form-inline mx-lg-3" /*onSubmit={this.queryServer}*/>
                <div className="form-group">
                    <input className="form-control" 
                           id="query" 
                           /*value={this.state.queryTerms}
                           onChange={this.handleQuery}*/
                           placeholder="Query"></input>
                </div>
                <button type="submit" className="btn btn-primary">Search</button>
            </form>
        );
    }
}

export default class SearchResults extends React.Component {

    render () {
        return (
            <div>
                <SearchBar />
                <ResultsMediaList results={this.props.results} /> 
            </div>
        );
    }
}


