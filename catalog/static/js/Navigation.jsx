import React from "react";

class Logo extends React.Component {
    render () {
        return (
            <div>
                <a class="navbar-brand" href="{this.props.base_url}">Navbar</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse"
                     data-target="#navbarSupportedContent" 
                     aria-controls="navbarSupportedContent" aria-expanded="false"
                     aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        );
    }

}

export default class NavigationBar extends React.Component {

    render () {
        return (
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <Logo base_url="http://bibcat.org/" />
                <p>Lorem ipsum dolor sit amet</p>
            </nav>
        );   
    }
}
