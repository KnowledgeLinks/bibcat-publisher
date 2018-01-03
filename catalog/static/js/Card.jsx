import React from "react";

class CardBody extends React.Component {
    render() {
        return (
            <div class="card-body"></div>
        );
    }
}

class CardFooter extends React.Component {
    render() {
        return (
            <div class="card-header">{this.props.title}</div>
        );
    }
}


class CardHeader extends React.Component {
    render() {
        return (
            <div class="card-header">{this.props.title}</div>
        );
    }
}

export default class Card extends React.Component {

    render () {
        return (
            <div class="card">
                <CardHeader />
                <CardBody />
                <CardFooter /
            </div>
        );
    }

}
