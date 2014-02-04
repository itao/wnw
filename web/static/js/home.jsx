/** @jsx React.DOM */

var HelloWorld = React.createClass({
  render: function() {
    return (
        <div>
            <h4>Hello, <input type="text" placeholder="Your name here" />!</h4>
            <h4>It is {this.props.date.toTimeString()}</h4>
        </div>
    );
  }
});

setInterval(function() {
  React.renderComponent(
    <HelloWorld date={new Date()} />,
    document.getElementById('example')
  );
}, 500);