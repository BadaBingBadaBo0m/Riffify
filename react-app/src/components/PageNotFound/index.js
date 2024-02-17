import React, { useEffect } from "react";
import { useParams } from "react-router-dom";

const get_404 = async (params) => {
  const res = await fetch(`/api/${params}`)
  const data = await res.json()
  console.log(data)
}

const PageNotFound = () => {
  const params = useParams();
  get_404(params)

  useEffect(() => {
    document.title = "Page not found"
  }, [])

  return (
    <div>
      <h2>Page not found</h2>
      {/* <button onClick={() => console.log('bruh', params)}>Bruh</button> */}
    </div>
  )
}

export default PageNotFound;