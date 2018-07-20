/**
 * HV_Trees.java
 * Outputs an HV-tree of a given order and factor.
 *
 * @author  Max Huang
 * @version 1.0
 * @since   11 July 2018
 */

public class HVTrees extends LinesComponent {

    private static final long serialVersionUID = 1L;

	/**
     * @param args - order of argumnets is 'order' then 'factor' value.
     */
    public static void main(String[] args) {
        int order, factor;
        final int LENGTH = 5;
        if (args.length > 0 && args.length <= 2) {
            try {
                order = Integer.parseInt(args[0]);
                factor = Integer.parseInt(args[1]);
            } catch (NumberFormatException e) {
                System.err.println(e);
                System.exit(1);
            }


        }

    }


}