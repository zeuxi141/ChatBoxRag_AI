import { useLayoutEffect, useState } from "react";

function Mount() {
  const [count, setCount] = useState(0);
  useLayoutEffect(() => {
    if (count > 3) setCount(0);
  }, [count]);

  return (
    <div>
      <div>{count}</div>
      <button
        onClick={() => {
          setCount(count + 1);
        }}
      >
        Tăng
      </button>
      4{" "}
    </div>
  );
}
export default Mount;
