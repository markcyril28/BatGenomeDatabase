import React from "react";
import StrainList from "../../components/strain_content/StrainList";
import Sidebar from "../../components/sidebar/Sidebar";
import "./Strain.css";
import { useParams } from "react-router-dom";

export default function Strain(props) {
  let { id } = useParams();

  return (
    <>
      <Sidebar Crumb={props.Crumb} match={id} />
      <div className="strain_content">
        <h1 className="title">Strain Database</h1>
        <StrainList />
      </div>
    </>
  );
}
