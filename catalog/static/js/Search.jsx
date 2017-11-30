function Search(props) {
    return (
        <form className="form-inline mx-lg-3">
            <div className="form-group">
                <input className="form-control" id="query" placeholder="Query"></input>
            </div>
            <button type="submit" className="btn btn-primary">Search</button>
        </form>
    );
}
