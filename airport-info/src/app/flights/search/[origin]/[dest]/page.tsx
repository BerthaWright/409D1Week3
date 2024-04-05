export default function AirportInfo({ params }: {params:  {origin: string, dest:string}  }){
    return (
        <div>Searching for flights from {params.origin} to {params.dest}</div>
    ); 
}