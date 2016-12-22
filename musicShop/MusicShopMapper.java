import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

/*
 * Mapper to find out number of unique listener
 */
public class MusicShopMapper extends Mapper<Object, Text, IntWritable, IntWritable>{

	IntWritable trackID = new IntWritable();
	IntWritable userID = new IntWritable();
	
	@Override
	public void map(Object key, Text value, Context context)
		throws IOException, InterruptedException{
		
		String[] parts = value.toString().split("[|]");
	
		trackID.set(Integer.parseInt(parts[MusicConstants.TRACK_ID]));
		userID.set(Integer.parseInt(parts[MusicConstants.USER_ID]));
		
		if(parts.length == 5){
			context.write(trackID, userID);
			System.out.println(trackID);
		}else {
	        // add counter for invalid records
	        context.getCounter(COUNTERS.INVALID_RECORD_COUNT).increment(1L);
	    }
		
	}	
}
