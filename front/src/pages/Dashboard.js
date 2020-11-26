import ReactPlayer from "react-player";
import { FaChartBar, FaStickyNote, FaPlus } from "react-icons/fa";

function Dashboard() {
    return (
        <div className="App-wrapper">
            <header className="App-header">
                <h1>Dashboard</h1>
            </header>
            <div className="App-contents">
                <div className="App-player">
                    <ReactPlayer url='https://www.youtube.com/watch?v=ysz5S6PUM-U' width='100%' height='100%'/>
                </div>
                <div className="App-sidebar">
                    <h2>Metrics</h2>
                    <div className="App-metrics">
                        <span className="temperature">Temperature: <br/> 67.1 F / 19.5 C</span>
                        <span className="humidity">Humidity: 47</span>
                        <button className="App-btn"><FaChartBar/> Details</button>
                        <hr/>
                    </div>
                    <div className="App-note-buttons">
                        <button className="App-btn"><FaStickyNote/> Notes</button><br/>
                        <button className="App-btn"><FaPlus/> Add Note</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Dashboard;